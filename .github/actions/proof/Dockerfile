# syntax=docker/dockerfile:latest

FROM debian:bullseye-slim
# Install dependencies.
RUN apt update -y && apt install git wget zstd -y
# Add a user.
RUN useradd -m lean
COPY entrypoint.sh /home/lean/entrypoint.sh
# Add execute permissions on the entrypoint.sh file.
RUN chmod +x /home/lean/entrypoint.sh
# Change ownership.
RUN chown lean:lean /home/lean/entrypoint.sh
# Retrieve Lean.
RUN wget -q https://github.com/leanprover/lean4/releases/download/v4.0.0-m5/lean-4.0.0-linux.tar.zst -O /home/lean/lean-4.0.0-linux.tar.zst
# Extract files from the archive.
RUN tar axf /home/lean/lean-4.0.0-linux.tar.zst --directory=/home/lean
# Remove the archive.
RUN rm /home/lean/lean-4.0.0-linux.tar.zst
# Change ownership.
RUN chown -hR lean:lean /home/lean/lean-4.0.0-linux

ENTRYPOINT ["/home/lean/entrypoint.sh","/github/workspace/docs/proof/.lean"]