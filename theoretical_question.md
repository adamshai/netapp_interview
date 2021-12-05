# Theoretical Part (NO CODE)

Now we would like to collect usage-log, of our API (in your service), as used by our users.<br/>

- We want to log all requests, even if they had failed
- We want to be able to identify the order of which a specific user, used our API (assume that<br/>
  there is a authentication mechanism)
- We may have multiple instances of the server you created
- In the future we would want to run analytics over those logs, so it would be a nice benefit to<br/>
  have easy and simple access to them

## Questions

1. How would you implement it? where would you store it?
2. What would you do differently in a much larger scale of data and usage

## Answers

> 1. How would you implement it? where would you store it?

We want to log events per API request and API response

### Event info

The event should include:

- timestamp : timestamp
- request URI : str
- user ID : str
- distributed trace ID (if relevant) : str
- mahcine ID : str
- process/instance ID : str
- cluster ID : str
- region ID : str
- request/response body : str
- is monitored : bool (optional, only for event handling purposes, see Storage)

### Recording events

If the infrastructure allows pre-request and pre-response hooks, we can record the events there.<br/>
Otherwise we can decorate our python functions with these hooks. We'll send the event info asynchronously<br/>
to an event queue

### Event queue

The role of the event queue would be to control the control the high volume of events. Kafka can<br/>
be a good candidate for an event queue

### Processing events and storage

We will have several stateless worker services to process the data from Kafka, a service will bulk<br/>
log entries and store them in a CSV file on a persistent storage, like S3. We can name the files<br/>
by their creation timestamps, and break them every 100MB of event data.

If we are monitoring an event, e.g. for debugging, we can also redirect the event to a database<br/>
for easy access. A quick way to do this is just to create a new Kafka stream and query<br/>
its KTable.

### Analytics

To analyze log info we'll have to use a UI and a database that would give us a good response time<br/>
for BI operations. We can load the relevant logs from S3 to Cassandra, use Spark to pull data<br/>
from it, and present it in Grafana, Tableau, Qlik, Splunk etc.

> 2. What would you do differently in a much larger scale of data and usage

In the case above we mentioned

- API processing, sending log events
- Kafka queuing
- Kafka event handlers
- storing events in a log file
- loading events to a database
- loading log files to a database
- querying the database for analytics

When we execute those actions in large scale we want to assure

- availability
- responsiveness
- correctness
- completeness

Availability we assure by dynamic scaling, provided by the infrastructure.

Responsiveness we assure by looking at the loads and adding load balancers or deploying instances<br/>
strategically closer to the services they interact with.

Correctness we can assure by replicating the data, storing a checksum per record. Kafka also keeps<br/>
a log of all events, we can compare hourly/daily stats and compare to the number of records saves<br/>
and in the worst case, to retrieve missing records from Kafka logs.

Completeness we can assure by repeating failing log requests, storing data on local machine, and<br/>
resending it when logging mechanism is live again

### Alerts

In addition to all that we can add alerting mechanism to track abnormal issues, either scenarios that<br/>
we hard code, or let the system come up with anomaly detection

### Note on data access

Access to data is tricky. It is dependent on the queries and the way the data is stored. For better<br/>
performance we can optimize our databases or queries ourselves but we can also use off the shelf <br/>
solutions like RedShift, Snowflake, etc.

### Note on scaling

We usually achieve scaling by replication, partitioning, sharding, and better data aware system design.<br/>
It allows us to scale but for a price. Identifying data access patterns can allow us to tweak the system<br/>
for better performance using the same resources, usually for the same price.

Other concerns will be synching systems, and having many moving parts in the system, so a hoslistic<br/>
code maintenance and deployment solution should be set up, with as much automation as possible.
