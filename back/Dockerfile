# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.9.7

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get the Real World example app
COPY . /srv/drf_src

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /srv/drf_src

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requierement.txt

VOLUME /drf_src

EXPOSE 8080

CMD python python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]