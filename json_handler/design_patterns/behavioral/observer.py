class Subject:
    def __init__(self):
        self.observers = []

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, data):
        for observer in self.observers:
            observer.update(data)

class NewsWebsite(Subject):
    def publish_article(self, title, content):
        print(f"Publishing new article: {title}")
        self.notify_observers({"title": title, "content": content})

class EmailObserver:
    def update(self, data):
        print(f"Sending email notification for new article: {data['title']}")

class MobileAppObserver:
    def update(self, data):
        print(f"Updating mobile app notification with new article: {data['title']}")

# Create website and observers
website = NewsWebsite()
email_observer = EmailObserver()
mobile_app_observer = MobileAppObserver()

# Register observers
website.register_observer(email_observer)
website.register_observer(mobile_app_observer)

# Publish an article and observe notifications
website.publish_article("Breaking News!", "Important content for subscribers.")


# Subject defines the interface for notifying observers.
# NewsWebsite inherits from Subject and publishes articles, notifying registered observers.
# EmailObserver and MobileAppObserver implement the update method to react to notifications with specific actions (sending emails, updating mobile app).
# Registering observers with the website establishes the subscription.
# When an article is published, notify_observers sends the article data to each observer's update method.