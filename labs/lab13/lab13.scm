; Lab 13: Final Review

; Q2
(define (rle s)
  (define (rle-helper s previous ct)
    (cond ((null? s)
           (if (zero? ct)
               nil
               (cons-stream (list previous ct) nil)
           )
          )
          ((not (equal? previous (car s)))
           (cons-stream (list previous ct) (rle s))
          )
          (else (rle-helper (cdr-stream s) previous (+ 1 ct)))
    )
  )
  (if (null? s)
    nil
    (rle-helper s (car s) 0)
  )
)

; Q2 testing functions
(define (list-to-stream lst)
    (if (null? lst) nil
                    (cons-stream (car lst) (list-to-stream (cdr lst))))
)

(define (stream-to-list s)
    (if (null? s) nil
                 (cons (car s) (stream-to-list (cdr-stream s))))
)

; Q3
(define (tail-replicate x n)
  (define (helper x n lst)
    (if (= n 0)
    lst
    (helper x (- n 1) (cons x lst))
    )
  )
  (helper x n nil)
)
