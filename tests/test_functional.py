# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/
"""


class TestHealthcheck:
    def test_that_application_handles_user_request(self, testapp):
        response = testapp.get("/healthcheck/", status="*")
        assert response is not None
        assert response.status_code == 200
