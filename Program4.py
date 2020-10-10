import timeit
import shelve

def timer(function):
  def new_function():
    start_time = timeit.default_timer()
    function()
    #elapsed = timeit.default_timer() - start_time
    end_time=timeit.default_timer()
    time=end_time-start_time

    print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=time))
  return new_function()

@timer
def dictionary():
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }


@timer
def shel():
    s = shelve.open('test_shelf.db')
    try:
        s['key1'] = {'int': 10, 'float': 9.5, 'string': 'Sample data'}
    finally:
        s.close()


