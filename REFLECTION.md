# Test Failure

FAIL: test_book_appears_on_books_page (catalog.tests.BookListTest.test_book_appears_on_books_page)

AssertionError: False is not true : Couldn't find 'Unique Testing Book' in the following response

Ran 1 test in 0.014s

FAILED (failures=1)

This failure showed me that my test correctly checks whether a book from the database appears on the Books page.

## Question 1

The Book model carries the ForeignKey that points to the Publisher model. I set it up this way because one publisher can publish many books, while each book belongs to one publisher. If I reversed it, each publisher would only point to one book instead of allowing multiple books to belong to the same publisher.

## Question 2

I chose an IntegerField for the page_count field because the number of pages is a whole number. This makes more sense than a CharField because an IntegerField stores the page count as a number. If I used a CharField, the page count would be treated as text instead.