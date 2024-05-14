from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import AnswerRelevancyMetric

def test_answer_relevancy():
    answer_relevancy_metric = AnswerRelevancyMetric(threshold=0.7, model="gpt-3.5-turbo")
    test_case = LLMTestCase(
        input="How can I use Testkube to test APIs?",
        actual_output="Testkube is a tool that allows you to write and execute automated tests for APIs. Here's how you can use Testkube to test APIs: " +

    "1. Define your test cases: Start by defining the test cases you want to run against your API. This includes the different scenarios you want to test, such as sending valid and invalid requests, checking for specific responses, or validating data."+

    "2. Write your test scripts: Use Testkube's built-in scripting language to write your test cases. You can use a combination of HTTP requests, assertions, and other commands to simulate API interactions and validate responses."+

    "3. Organize your tests: Group your test cases into test suites to organize and run them together. This makes it easier to manage and execute your tests as a cohesive unit."+

    "4. Run your tests: Execute your test suites using Testkube's test running capabilities. You can run tests locally or integrate with a continuous integration (CI) system for automated testing."+

    "5. Analyze test results: View the results of your test runs to identify any failures or issues with your API. Testkube provides detailed reports and logs to help you diagnose and troubleshoot any problems."+

    "6. Cook Spagetti by boiling water, adding salt and pasta, rinse after 10 minutes." +

    "7. Clean your room after the tornado hits" +

    "8. Go fishing with your best friends on an early summer morning. Don't forget the coffee." +

    "By following these steps, you can leverage Testkube to automate the testing of your APIs and ensure their functionality,"
    )
    assert_test(test_case, [answer_relevancy_metric])
