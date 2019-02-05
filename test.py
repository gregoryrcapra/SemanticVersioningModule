from SemVer import SemVer

def greater_or_less_tests(semVerObject):
    assert SemVer.compare(semVerObject,'1.3.6 1.4.5') == 'after'
    assert SemVer.compare(semVerObject, '1.9.6 1.6.9') == 'before'
    assert SemVer.compare(semVerObject, '10.0.0 9.9.9    ') == 'before'
    assert SemVer.compare(semVerObject, '1.4.5-alpha    1.4.5-beta') == 'after'
    assert SemVer.compare(semVerObject, '1.4.5-betaz 1.4.5-beta') == 'before'
    assert SemVer.compare(semVerObject, '1.4.5-alpha+dummy.meta.data 1.4.5-beta') == 'after'

def equality_tests(semVerObject):
    assert SemVer.compare(semVerObject, '1.3.6 1.3.6') == 'equal'
    assert SemVer.compare(semVerObject, '1.9.6-alpha 1.9.6-alpha') == 'equal'
    assert SemVer.compare(semVerObject, '10.0.0-alpha.33.zz 10.0.0-alpha.33.zz') == 'equal'
    assert SemVer.compare(semVerObject, '1.4.5-alpha+33.rr.t4 1.4.5-alpha+hello.world') == 'equal'
    assert SemVer.compare(semVerObject, '1.4.5-beta 1.4.5-beta+hello.world.99') == 'equal'

def invalid_input_tests(semVerObject):
    assert SemVer.compare(semVerObject, '1.3.6') == 'invalid'
    assert SemVer.compare(semVerObject, '1.9.6-alpha 1.9.6-alpha  1.55.5') == 'invalid'
    assert SemVer.compare(semVerObject, '10.0.0-alpha....33.zz 12.3.4') == 'invalid'
    assert SemVer.compare(semVerObject, '1.4.5-') == 'invalid'
    assert SemVer.compare(semVerObject, '1.4.5+') == 'invalid'

if __name__ == '__main__':
    dummy = SemVer('')
    greater_or_less_tests(dummy)
    equality_tests(dummy)
    invalid_input_tests(dummy)
    userInput = input("Please enter a string input for semantic version comparison: ")
    SemVer.compare(dummy,userInput)
