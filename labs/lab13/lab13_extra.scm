; Lab 13: Final Review - Optional Questions

; Q5
(define (compose-all funcs)
  'YOUR-CODE-HERE
)

; Q6
(define (deep-map fn s)
  'YOUR-CODE-HERE
)

; Q7
; Feel free to use these helper procedures in your solution
(define (map fn s)
  (if (null? s) nil
      (cons (fn (car s))
            (map fn (cdr s)))))

(define (filter fn s)
  (cond ((null? s) nil)
        ((fn (car s)) (cons (car s)
                            (filter fn (cdr s))))
        (else (filter fn (cdr s)))))

; Implementing and using these helper procedures is optional. You are allowed
; to delete them.
(define (unique s)
  'YOUR-CODE-HERE
)

(define (count name s)
  'YOUR-CODE-HERE
)

(define (tally names)
  'YOUR-CODE-HERE
)

; Q8
(define (insert n s)
  'YOUR-CODE-HERE
)