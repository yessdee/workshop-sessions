#include <linux/module.h>

int init_module(void)
{
	printk("Hello World\n");
	return 0;
}

void cleanup_module(void)
{
	printk("Goodbye World\n");
}

