#include "lists.h"
/**
 * is_palindrome - ......
 * @head: the head of the list.
 * Return:0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int arr[200], i = 0, j = 0;

	ptr = *head;
	if (ptr == NULL)
		return (1);
	while (ptr != NULL)
	{
		arr[i] = ptr->n;
		ptr = ptr->next;
		i++;
	}
	i--;
	while (j < i)
	{
		if (arr[j] == arr[i])
		{
			j++;
			i--;
			continue;
		}
		return (0);
	}

	return (1);
}
