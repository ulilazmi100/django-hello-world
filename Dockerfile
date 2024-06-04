FROM python:3.12-bullseye AS base
RUN pip install pdm
FROM oven/bun:1 as style_builder
WORKDIR /app
COPY . .
RUN bun install
RUN bun run build
# RUN-
FROM base AS builder
WORKDIR /app
COPY . .
# COPY --from=style_builder /app/src/landing/static/landing/tailwind.css /app/src/landing
RUN pdm install
RUN pdm run src/manage.py collectstatic --noinput
EXPOSE 8000
CMD [pdm, run, src/manage.py, runserver, ""]