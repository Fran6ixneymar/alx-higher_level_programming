#include "lists.h"

/**
 * check_cycle - This function checks if a cycle is contained in a linked list.
 * @list: Points to the beginning of the node.
 *
 * Return: 1 if there is a cycle, 0 if none.
 */
int check_cycle(listint_t *list)
{
	listint_t *old = list;
	listint_t *new = list;

	if (!list)
		return (0);

	while (old && new && new->next)
	{
		old = old->next;
		new = new->next->next;
		if (old == fast)
			return (1);
	}

	return (0);
}
