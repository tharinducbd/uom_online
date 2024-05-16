from datetime import date, timedelta


def _is_library_member(member_id):
    return


def _get_lent_books(member_id):
    return


def _is_member_eligible_to_lend(member_id):
    max_books_to_lend = 2

    if not _is_library_member(member_id):
        print("User not eligible: user is not a member")
        return False

    books_lent = _get_lent_books(member_id)
    if len(books_lent) == max_books_to_lend:
        print("User not eligible: cannot lend more than 2 books")
        return False

    return True


def _is_book_available(book_id):
    return


def _get_return_date():
    lend_time_period = 14
    current_date = date.today()
    return current_date + timedelta(days=lend_time_period)


def _checkout_book(book_id, member_id, return_date):
    return


def lend_book(member_id, book_id):
    # lend book if only elegible
    if _is_member_eligible_to_lend(member_id):
        if _is_book_available(book_id):
            return_date = _get_return_date()
            _checkout_book(book_id, member_id, return_date)
            print("Book lent for member successfully!")
        else:
            print("Book not available")
