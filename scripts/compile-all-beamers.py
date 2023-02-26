#!/bin/python3
from courses import Courses

for course in Courses():
    beamers = course.beamers

    r = beamers.parse_range_string('all')
    beamers.update_lectures_in_master(r)
    beamers.compile_master()
