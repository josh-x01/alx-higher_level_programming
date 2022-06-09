#include "lists.h"
#include <stdio.h>

/**
 * print_dlistint - print all element in double linked list
 * @h: the of the linked list
 * Return: the number of elements
 */

size_t print_dlistint(const dlistint_t *h)
{
	int size = 0;

	while (h != NULL)
	{
		printf("%d\n", h->n);
		h = h->next;
		size++;
	}
	return (size);
}
