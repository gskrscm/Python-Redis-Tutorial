# Install redis for Python
`pip install redis`

# Next, write your code
Use this example as a reference.

# Run your redis server in WSL or Linux
```
$ sudo apt-get install -y redis
$ redis-server
```

# Finally, run your code when you know redis is up.
Useful commands for `redis-cli`:
- `keys *` to list keys
- `get [key]` to get a key
- `del [key]` to delete a key
- `ttl [key]` to see how long until a key expires in seconds