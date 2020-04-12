# Initialize a Python image
FROM python:3.8-alpine

# Add file to the image filesystem at a path
ADD password_generator.py /tmp/

# Additional commands to execute image
RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv lock --requirements > /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Execute commands when the image loads
CMD [ "python", "./tmp/password_generator.py" ]
