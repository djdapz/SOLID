import os
from behave import given, step, when, then
from hamcrest import assert_that, is_

from open_closed_principle.EvenLineReader import EvenLineReader
from open_closed_principle.LineReader import LineReader
from src.single_responsibility_principle.FileReader import FileReader
from src.single_responsibility_principle.FileReporter import FileReporter


@step("a reader for {input_file}")
def step_impl(context, input_file):
    context.reader = FileReader("resources/" + input_file)


@given("a line reader for {input_file}")
def step_impl(context, input_file):
    context.reader = LineReader("resources/" + input_file)


@given("a every other line reader for {input_file}")
def step_impl(context, input_file):
    context.reader = EvenLineReader("resources/" + input_file)


@step('a reporter that writes {input_file} to {output_file}')
def step_impl(context, input_file, output_file):
    context.subject = FileReporter("resources/" + output_file, context.reader.read())


@when("we generate a report")
def step_impl(context):
    context.subject.report()


@then('{file} should be created')
def step_impl(context, file):
    assert_that(os.path.isfile(file), is_(True))


@step('{file} does not exist')
def step_impl(context, file):
    assert_that(os.path.isfile(file), is_(False))


@given('there is no {file}')
def step_impl(context, file):
    if os.path.isfile(file):
        os.remove(file)
    assert_that(os.path.isfile(file), is_(False))


@step('we have an {file} with content {content}')
def step_impl(context, file, content):
    verify_file_equals(content, file)


@step('we have a multiline file {file} with content {content}')
def step_impl(context, file, content):
    content = content.replace("\\n", "\n")
    verify_file_equals(content, file)


def verify_file_equals(content, file):
    resources_file = "resources/" + file
    assert_that(os.path.isfile(resources_file), is_(True))
    assert_that(open(resources_file, "+r").read(), is_(content))


@when("we want to read the contents of {file_name}")
def step_impl(context, file_name):
    context.subject = FileReader("resources/" + file_name)


@then("we find the the contents is {content}")
def step_impl(context, content):
    assert_that(context.subject.read(), is_(content))
