# Start from the base image
FROM ubuntu:20.04

# Set the working directory
WORKDIR /app

# Copy a local file using COPY
COPY myfile.txt /app/

# Copy a directory using COPY
COPY mydirectory /app/

# Add a file from a remote URL using ADD
ADD http://example.com/file.zip /app/

# Automatically extract a tar archive using ADD
ADD myarchive.tar.gz /app/

# Set the user to 'myuser'
USER myuser

# Command to run when the container starts
CMD ["bash"]
