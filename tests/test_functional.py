# -*- coding: utf-8 -*-
"""Functional tests using WebTest.

See: http://webtest.readthedocs.org/

"""


class TestHealthcheck:
    """TestHealthcheck."""

    def test_request(self, testapp):
        """Resquest tests using WebTest."""
        response = testapp.get("/healthcheck/", status="*")
        assert response is not None
        assert response.status_code == 200
