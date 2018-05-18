# coding=utf-8
from zasterisk.base import DiscoveryFieldCommand


class Command(DiscoveryFieldCommand):
    help = '''
        PJSIP peers
    '''

    def discovery(self, ami):
        def callback(connect, timeout):
            events = self.parse_events(connect)
            return self.create_discovery(events.get("EndpointList"), "{#USERNAME}", "ObjectName")

        return ami.execute("PJSIPShowEndpoints", {}, callback)

    def get_field(self, ami, field_name, param):
        return ami.execute("PJSIPShowEndpoint", {"Endpoint": param}, lambda connect, timeout: self.expect_field(
            connect, field_name, timeout))

    def count(self, ami):
        return 0


