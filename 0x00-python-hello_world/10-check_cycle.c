#include "lists.h"

/**
 * check_cycle - This function checks if a cycle is contained in a linked list.
 * @list: Points to the beginning of the node.
 *
 * Return: 1 if there is a cycle, 0 if none.
 */
int check_cycle(listint_t *list)
{
	listint_t *new, *old;

	if (list == NULL || list->next == NULL)
		return (0);
	new = list;
	old = new->next;

	while (new != NULL && old->next != NULL
		&& old->next->next != NULL)
	{
		if (new == old)
			return (1);
		new = new->next;
		old = old->next->next;
	}
	return (0);
}
