#include "lists.h"

/**
 * insert_node - This inserts into a sorted singly-linked list a number.
 * @head: Points to the head of the linked list.
 * @number: Number to insert.
 *
 * Return: NULL -If the function fails.
 * Otherwise - Points to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *start;

	start = malloc(sizeof(listint_t));
	if (start == NULL)
		return (NULL);
	start->n = number;

	if (node == NULL || node->n >= number)
	{
		start->next = node;
		*head = start;
		return (start);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	start->next = node->next;
	node->next = start;

	return (start);
}
