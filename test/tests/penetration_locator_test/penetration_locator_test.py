from options import *

test = { INPUT : 'penetration_locator_test.i',
         EXODIFF : ['out.e'] }

parallel_test = { INPUT : 'penetration_locator_test.i',
                  EXODIFF : ['out.e'],
                  MAX_PARALLEL : '3',
                  PREREQ : 'test' }

