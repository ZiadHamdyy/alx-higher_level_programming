#include "lists.h"
/**
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *ptr;

	
	current = malloc(sizeof(listint_t));
	current->n = number;
	if (head == NULL)
	{
		*head = current;
		return(current);
	}
	ptr = *head;
	while (ptr != NULL && number > ptr->next->n)
	{
		ptr = ptr->next;
	}
	current->next = ptr->next;
	ptr->next = current;
	return(current);
}
