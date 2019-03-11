import os
from behave import given, step, when, then
from hamcrest import assert_that, is_

from src.single_responsibility_principle.main import FileReporter


@step('a reporter that writes {input_file} to {output_file}')
def step_impl(context, input_file, output_file):
    with open("resources/" + input_file) as input_file_contents:
        context.subject = FileReporter("resources/" + output_file, input_file_contents.read())


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
    resources_file = "resources/" + file
    assert_that(os.path.isfile(resources_file), is_(True))
    assert_that(open(resources_file, "+r").read(), is_(content))