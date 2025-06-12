FROM public.ecr.aws/amazonlinux/amazonlinux:2023

# Install Python 3 and essential libraries
RUN yum update -y && \
    yum install -y python3 python3-pip gcc make libffi-devel openssl-devel && \
    pip3 install --upgrade pip

# Set working directory inside the container
WORKDIR /app

# Copy project files into container
COPY . /app

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Run the app with Flask (adjust this line if needed)
ENV FLASK_APP=application.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
