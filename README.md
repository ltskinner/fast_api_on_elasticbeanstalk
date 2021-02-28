# Fast API running on AWS Elastic Beanstalk

Example of deploying a [Fast API](https://fastapi.tiangolo.com/) instance to AWS Elastic Beanstalk

## Components

### application.py

This is the actual file that runs the api server

Here, the main component is the __main__ sequence:

```python
if __name__ == '__main__':
    app.app.run()  # Without this call, the server wont run correctly on AWS
```

### requirements.txt

These are the packages AWS Elastic Beanstalk will install upon launch

```txt
fastapi
uvicorn[standard]  # MUST install the [standard] extensions
websockets         # MUST install this as well, or will error out
```

### Procfile

This configures the server run process, and without it the app will not run correctly

```Procfile
web: uvicorn application:app --host=0.0.0.0 --ws websockets
```

## Deployment

Must zip the following files into a directory

**Note** these must be at the top level of the zipped file

* 1. [ ] Upload package to AWS ELB environment
* 2. [ ] Configure software section for the WSGIPath to be `application` (of application.py)

### First, navigate to the software config section

![alt text](./docs/config_software.png)

### Next, set the WSGIPath

![alt text](./docs/wsgi_path.png)
