def run(self):
        try:
            self.sse = ClosableSSEClient(self.url)
            for msg in self.sse:
                event = msg.event
                if event is not None and event in ('put', 'patch'):
                    response = json.loads(msg.data)
                    if response is not None:
                        # Default to CHILD_CHANGED event
                        occurred_event = FirebaseEvents.CHILD_CHANGED
                        if response['data'] is None:
                            occurred_event = FirebaseEvents.CHILD_DELETED

                        # Get the event I'm trying to listen to
                        ev = FirebaseEvents.id(self.event_name)
                        if occurred_event == ev or ev == FirebaseEvents.CHILD_CHANGED:
                            self.callback(event, response)
        except socket.error:
            pass 
