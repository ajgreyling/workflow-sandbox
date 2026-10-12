from behave import given, then, when
from fastapi.testclient import TestClient

from app.main import app


@given("the app is running")
def step_app_running(context):
    context.client = TestClient(app)


@when('I request "{path}"')
def step_request(context, path):
    context.response = context.client.get(path)


@then("the response status is {status:d}")
def step_response_status(context, status):
    assert context.response.status_code == status
