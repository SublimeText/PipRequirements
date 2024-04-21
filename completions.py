# Don't evaluate type annotations at runtime
from __future__ import annotations

import sublime
import sublime_plugin

from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sublime_types import Point

KIND_PIP_ARGUMENTS = [sublime.KIND_ID_VARIABLE, "v", "Argument"]


class CompletionsProvider(sublime_plugin.EventListener):
    """
    This class describes a completions provider.

    Provide pip CLI arguments completions as putting them into *.sublime-completions
    doesn't work due to leading hyphens.
    """

    def on_query_completions(
        self,
        view: sublime.View,
        prefix: str,
        locations: list[Point]
    ):
        location = locations[0]
        selector = "text.pip-requirements & (meta.expect-option-or-package | variable.parameter)"
        if any(view.match_selector(pt, selector) for pt in (location, location - 1)):
            return self.pip_arguments

    @cached_property
    def pip_arguments(self):
        return sublime.CompletionList([
            sublime.CompletionItem(
                trigger="--config-settings",
                kind=KIND_PIP_ARGUMENTS,
                details="Configuration settings to be passed to the PEP 517 build backend.",
            ),
            sublime.CompletionItem(
                trigger="--constraint",
                kind=KIND_PIP_ARGUMENTS,
                details="Constrain versions using the given constraints file.",
            ),
            sublime.CompletionItem(
                trigger="--editable",
                kind=KIND_PIP_ARGUMENTS,
                details="Install a project in editable mode (i.e. setuptools “develop mode”) from a local project path or a VCS url.",
            ),
            sublime.CompletionItem(
                trigger="--extra-index-url",
                kind=KIND_PIP_ARGUMENTS,
                details="Extra URLs of package indexes to use in addition to --index-url.",
            ),
            sublime.CompletionItem(
                trigger="--find-links",
                kind=KIND_PIP_ARGUMENTS,
                details="If a URL or path to an html file, then parse for links to archives",
            ),
            sublime.CompletionItem(
                trigger="--global-option",
                kind=KIND_PIP_ARGUMENTS,
                details="Extra global options to be supplied to the setup.py call before the install or bdist_wheel command.",
            ),
            sublime.CompletionItem(
                trigger="--hash",
                kind=KIND_PIP_ARGUMENTS,
                details="for hash checking mode",
            ),
            sublime.CompletionItem(
                trigger="--index-url",
                kind=KIND_PIP_ARGUMENTS,
                details="Base URL of the Python Package Index",
            ),
            sublime.CompletionItem(
                trigger="--no-binary",
                kind=KIND_PIP_ARGUMENTS,
                details="Do not use binary packages.",
            ),
            sublime.CompletionItem(
                trigger="--no-index",
                kind=KIND_PIP_ARGUMENTS,
                details="Ignore package index",
            ),
            sublime.CompletionItem(
                trigger="--only-binary",
                kind=KIND_PIP_ARGUMENTS,
                details="Do not use source packages.",
            ),
            sublime.CompletionItem(
                trigger="--pre",
                kind=KIND_PIP_ARGUMENTS,
                details="Include pre-release and development versions.",
            ),
            sublime.CompletionItem(
                trigger="--prefer-binary",
                kind=KIND_PIP_ARGUMENTS,
                details="Prefer binary packages over source packages, even if the source packages are newer.",
            ),
            sublime.CompletionItem(
                trigger="--require-hashes",
                kind=KIND_PIP_ARGUMENTS,
                details="Require a hash to check each requirement against, for repeatable installs.",
            ),
            sublime.CompletionItem(
                trigger="--requirement",
                kind=KIND_PIP_ARGUMENTS,
                details="Install from the given requirements file.",
            ),
            sublime.CompletionItem(
                trigger="--trusted-host",
                kind=KIND_PIP_ARGUMENTS,
                details="Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.",
            ),
            sublime.CompletionItem(
                trigger="--use-feature",
                kind=KIND_PIP_ARGUMENTS,
                details="Enable new functionality, that may be backward incompatible.",
            ),
            sublime.CompletionItem(
                trigger="-c",
                kind=KIND_PIP_ARGUMENTS,
                details="Constrain versions using the given constraints file.",
            ),
            sublime.CompletionItem(
                trigger="-e",
                kind=KIND_PIP_ARGUMENTS,
                details="Install a project in editable mode (i.e. setuptools “develop mode”) from a local project path or a VCS url.",
            ),
            sublime.CompletionItem(
                trigger="-f",
                kind=KIND_PIP_ARGUMENTS,
                details="If a URL or path to an html file, then parse for links to archives",
            ),
            sublime.CompletionItem(
                trigger="-i",
                kind=KIND_PIP_ARGUMENTS,
                details="Base URL of the Python Package Index",
            ),
            sublime.CompletionItem(
                trigger="-r",
                kind=KIND_PIP_ARGUMENTS,
                details="Install from the given requirements file.",
            ),
        ])
