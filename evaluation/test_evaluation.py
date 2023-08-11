import os
import pytest
import xmlrunner
import evaluation

def test_add():
    assert evaluation.add(2, 3) == 5

def test_subtract():
    assert evaluation.subtract(5, 3) == 2

if __name__ == '__main__':
    # Run tests and generate JUnit XML report
    if not os.path.exists('test-results'):
        os.makedirs('test-results')
    with open('test-results/test_results.xml', 'wb') as output:
        pytest.main(['--junitxml=test-results/test_results.xml'])
    output.close()