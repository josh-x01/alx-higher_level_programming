#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - Return is a list s palindrome or not
 * @head:  double ponter to head
 *
 * Return: 1 on success
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int count, i;
	int nums[10000];

	current = *head;
	count = 0;

	if (*head == NULL)
		return (1);

	while (current != NULL)
	{
		nums[count] = current->n;
		current = current->next;
		count++;
	}

	for (i = 0; i < count; i++)
	{
		if (nums[i] == nums[count - 1])
			count--;
		else
			return (0);
	} return (1);
}
