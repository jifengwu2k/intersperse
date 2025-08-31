# coding=utf-8
# Copyright (c) 2025 Jifeng Wu
# Licensed under the MIT License. See LICENSE file in the project root for full license information.
from typing import Iterable, Iterator, TypeVar


T = TypeVar('T')
def intersperse(iterable, separator):
    # type: (Iterable[T], T) -> Iterator[T]
    """
    Yield the elements of iterable, inserting a separator between each pair of elements.

    Args:
        iterable (Iterable[T]): The input iterable whose elements will be interspersed.
        separator (T): The separator value to insert between each element.

    Yields:
        T: Elements from the original iterable, with separator values between them.

    Examples:
        >>> list(intersperse([1, 2, 3], 0))
        [1, 0, 2, 0, 3]

        >>> list(intersperse([], 0))
        []

        >>> list(intersperse([1], 0))
        [1]
    """
    iterator = iter(iterable)
    sentinel = object()

    # The first element or the sentinel
    first_element_or_sentinel = next(iterator, sentinel)
    if first_element_or_sentinel is not sentinel:
        yield first_element_or_sentinel

        # Yield the remaining elements
        for remaining_element in iterator:
            yield separator
            yield remaining_element
