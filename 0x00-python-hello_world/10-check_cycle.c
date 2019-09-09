#include "lists.h"

/**
 * check_cycle - checks if a linked list has a loop
 * @list: pointer to a linked list
 * Return: 1 if true, 0 otherwise
 */

int check_cycle(listint_t *list)
{
	listint_t *new, *new2;

	if (list == NULL)
		return (0);
	new = list;
	new2 = list;

	while (new->next != NULL && new2->next != NULL && new2->next->next != NULL)
	{
		new = new->next;
		new2 = new2->next->next;
		if (new == new2)
			return (1);
	}
	return (0);
}
