# Project Statement & Boundaries

## Problem Statement
Traditional terminal-based casual mini-games are frequently implemented as isolated, single-use scripts. This decoupled approach forces users to execute entirely separate programs to switch games, provides zero unified state tracking, and relies on brittle inputs where a single mistyped character causes a runtime crash (`ValueError`), wiping out all session progress.

## Scope of the Project
The architectural boundaries of the Playworld system cover:
* **Centralized Command Execution:** A unified terminal interface routing selections based on index codes or text aliases.
* **Deterministic Rule Engine:** Isolated operational scopes executing game logic matrices.
* **Exception Resilience:** Interception of illegal format entries to preserve application operational safety.

## Target Users
* **Students & Educators:** Individuals looking for simple, well-documented references for structured algorithmic flows and basic Python game programming.
* **Casual Players:** Terminal-based desktop operators seeking quick, lightweight entertainment without installing bulky graphical applications.

## High-Level Features
* Dynamic main menu router.
* String alignment system (`.strip().lower()`).
* Safe numeric boundary input catcher blocks.
