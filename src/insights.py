from numbers import Number
from src.jobs import read


def get_unique_job_types(path):
    lista = read(path)
    job_types = list()
    for row in lista:
        if not job_types.__contains__(dict.get(row, 'job_type')):
            job_types.append(dict.get(row, 'job_type'))
    return job_types


def filter_by_job_type(jobs, job_type):
    filtered_jobs = list()
    for row in jobs:
        if row['job_type'] == job_type:
            filtered_jobs.append(row)
    return filtered_jobs


def get_unique_industries(path):
    lista = read(path)
    result = list()
    for row in lista:
        if not row['industry'] in result and row['industry'] != '':
            result.append(row['industry'])
    return result


def filter_by_industry(jobs, industry):
    filtered_industry = list()
    for row in jobs:
        if row['industry'] == industry:
            filtered_industry.append(row)
    return filtered_industry


def get_max_salary(path):
    lista = read(path)
    max_sal = list()
    for row in lista:
        if not row['max_salary'].isdigit():
            continue
        max_sal.append(int(row['max_salary']))
    return max(max_sal)


def get_min_salary(path):
    lista = read(path)
    min_sal = list()
    for row in lista:
        if not row['min_salary'].isdigit():
            continue
        min_sal.append(int(row['min_salary']))
    return min(min_sal)


def matches_salary_range(job, salary):
    if 'min_salary' not in job or 'max_salary' not in job:
        raise ValueError('error')
    if not Number.__eq__(salary, int):
        raise ValueError('error')
    if type(job['min_salary']) != int or type(job['max_salary']) != int:
        raise ValueError('error')
    if int(job['min_salary']) > int(job['max_salary']):
        raise ValueError('error')

    return salary in range(int(job["min_salary"]), int(job["max_salary"]))


def filter_by_salary_range(jobs, salary):
    filtered_salary = list()
    for row in jobs:
        try:
            if matches_salary_range(row, salary):
                filtered_salary.append(row)
        except ValueError:
            continue
    return filtered_salary
