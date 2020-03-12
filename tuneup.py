#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = 'Rob Spears (GitHub: Forty9Unbeaten)'

import cProfile
import pstats
import functools
import timeit


def profile(func):
    '''A function that can be used as a decorator to measure performance'''
    @functools.wraps(func)
    def pro_wrapper(*args, **kwargs):
        pro = cProfile.Profile()
        pro.enable()
        duplicates = func(*args, **kwargs)
        pro.disable()
        stats = pstats.Stats(pro)
        stats.strip_dirs().sort_stats('cumulative').print_stats(2)
        return duplicates
    return pro_wrapper


def read_movies(src):
    '''Returns a list of movie titles'''
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


# uncomment next line to decorate function with time measurement statistics
# @profile
def find_duplicate_movies(src):
    '''Returns a list of duplicate movies from a src list'''
    movies = read_movies(src)
    duplicates = []
    while movies:
        title = movies.pop()
        if title in movies:
            duplicates.append(title)
            movies.remove(title)
    return duplicates


def timeit_helper():
    '''Part A:  Obtain some profiling measurements using timeit'''
    number = 2
    repeat = 3
    t = timeit.Timer(stmt='''t.main()''',
                     setup='''import tuneup as t''')
    results = t.repeat(number=number, repeat=repeat)
    min_time = min([res/number for res in results])
    print(
        '\n\tBest time across {} repeats of {} runs per repeat: {:.3f}'.format(
            repeat, number, min_time)
    )


def main():
    '''Computes a list of duplicate movie entries'''
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    # uncomment next line to gather time measurements with timeit module
    # timeit_helper()
    main()
