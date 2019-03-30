from zerver.lib.test_classes import WebhookTestCase

class BuildbotHookTests(WebhookTestCase):
    STREAM_NAME = "buildbot"
    URL_TEMPLATE = u"/api/v1/external/buildbot?api_key={api_key}&stream={stream}"
    FIXTURE_DIR_NAME = "buildbot"

    def test_build_started(self) -> None:
        expected_topic = "buildbot-hello"
        expected_message = "Build [#33](http://exampleurl.com/#builders/1/builds/33) for **runtests** started."
        self.send_and_test_stream_message("started", expected_topic, expected_message)

    def test_build_success(self) -> None:
        expected_topic = "buildbot-hello"
        expected_message = "Build [#33](http://exampleurl.com/#builders/1/builds/33) (result: success) for **runtests** finished."
        self.send_and_test_stream_message("finished_success", expected_topic, expected_message)

    def test_build_failure(self) -> None:
        expected_topic = "general"  # project key is empty
        expected_message = "Build [#34](http://exampleurl.com/#builders/1/builds/34) (result: failure) for **runtests** finished."
        self.send_and_test_stream_message("finished_failure", expected_topic, expected_message)
