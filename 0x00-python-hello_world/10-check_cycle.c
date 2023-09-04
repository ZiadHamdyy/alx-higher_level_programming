#include "lists.h"
/**
 * check_cycle - ..........
 * @list:the header of the list.
 * Return:1 if there is a circle or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr, *ptr2;
	int i = 0, j = 0;

	if (list == NULL)
		return (0);
	ptr = list;
	ptr2 = list;
	while (ptr != NULL)
	{
		ptr = ptr->next;
		for (j = 0 ; j < i; j++)
		{
			ptr2 = ptr2->next;
			if (ptr == ptr2)
			return (1);
		}
		ptr2 = list;
		i++;
	}
	return (0);
}
