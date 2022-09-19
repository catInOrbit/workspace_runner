FROM python:3.9-alpine as builder
ADD src/ /app
# COPY dist/ /temp/dist
WORKDIR /app
RUN pip install --target=/app requests
# RUN pip install --target=/app /temp/dist/*.whl

FROM python:3.9-alpine
COPY --from=builder /app/ /app
WORKDIR /app
ENV PYTHONPATH /app
CMD ["python", "/app/cli.py"]
