"""Entry point run inside each agent's container. Reads AGENT_MODULE and runs that agent's queue loop.

TODO: implement the queue-watcher loop (pull from Redis, call agent.process(), publish result).
"""
