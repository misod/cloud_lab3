from .tasks import longtime_add
import time

if __name__ == '__main__':
    result = longtime_add.delay(1,2)
    result1 = longtime_add.delay(2,2)
    result2 = longtime_add.delay(3,2)
    # at this time, our task is not finished, so it will return False
    print 'Task finished? ', result.ready()
    print 'Task result: ', result.result
    print 'Task finished? ', result1.ready()
    print 'Task result: ', result1.result
    print 'Task finished? ', result2.ready()
    print 'Task result: ', result2.result
    # sleep 10 seconds to ensure the task has been finished
    time.sleep(10)
    # now the task should be finished and ready method will return True
    print 'Task finished? ', result.ready()
    print 'Task result: ', result.result
    print 'Task finished? ', result1.ready()
    print 'Task result: ', result1.result
    print 'Task finished? ', result2.ready()
    print 'Task result: ', result2.result
