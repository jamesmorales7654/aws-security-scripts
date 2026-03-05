# AWS Security Scripts

Small automation scripts for identifying common security issues in AWS environments.

This repository contains simple examples of security automation using AWS APIs.

## Scripts

### public_sg_check.py
Detects security groups that allow public access (`0.0.0.0/0`).

This can help identify overly permissive network rules that expose resources to the internet.

## Technologies

- Python
- boto3
- AWS APIs

## Purpose

This repository demonstrates basic cloud security automation patterns that can be expanded into more advanced security tooling.
