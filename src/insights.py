from src.jobs import read

# from jobs import read


# helpers
def check_if_salary_range_is_number(min_salary, max_salary):
    return isinstance(min_salary, int) and isinstance(max_salary, int)


# requisitos
def get_unique_job_types(path):
    """Checks all different job types and returns a list of them.

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    unique_job_types = set()

    for job in read(path):
        unique_job_types.add(job["job_type"])
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    # Com a ajuda do Tulio na monitoria para refatoração
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    unique_industries = set()

    for job in read(path):
        if job["industry"] != "":
            unique_industries.add(job["industry"])
    return unique_industries


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    salaries = set()

    for salary in read(path):
        if salary["max_salary"].isnumeric():
            salary_value = int(salary["max_salary"])
            salaries.add(salary_value)
    max_salary = max(salaries)
    return max_salary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    salaries = set()

    for salary in read(path):
        if salary["min_salary"].isnumeric():
            salary_value = int(salary["min_salary"])
            salaries.add(salary_value)
    min_salary = min(salaries)
    return min_salary


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    # com ajuda do Bux na monitoria
    job_salaries_exists = "min_salary" in job and "max_salary" in job
    jobs_salaries_is_number = (
        job_salaries_exists
        and isinstance(job["min_salary"], int)
        and isinstance(job["max_salary"], int)
    )
    salary_is_number = isinstance(salary, int)
    min_salary_higher_than_max = (
        jobs_salaries_is_number and job["min_salary"] > job["max_salary"]
    )
    salary_is_in_range = (
        jobs_salaries_is_number
        and salary_is_number
        and job["min_salary"] <= salary <= job["max_salary"]
    )

    if salary_is_in_range:
        return True
    elif (
        not job_salaries_exists
        or not jobs_salaries_is_number
        or not salary_is_number
        or min_salary_higher_than_max
    ):
        raise ValueError("Check your inputs values. They must be integers")
    else:
        print(job, salary)
        return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """

    def handle_matches_salary_range(job, salary):
        try:
            if matches_salary_range(job, salary):
                return True
        except ValueError:
            pass

    return [job for job in jobs if handle_matches_salary_range(job, salary)]
