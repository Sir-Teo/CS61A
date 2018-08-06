;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Streams

(define (find s predicate)
  (if (predicate (car s))
    (car s)
    (if (not (equal? (cdr-stream s) nil))
        (find (cdr-stream s) predicate)
        #f
    )
  )
)

(define (scale-stream s k)
	(if (null? s)
		nil
		(cons-stream (* k (car s))
			(scale-stream
				(cdr-stream s)
				k)))
)

(define (has-cycle? s)
	(define (helper s prev)
		(if (null? s) #f
			(if (contains? prev (car s)) #t
				(helper (cdr-stream s) (cons-stream (car s) prev))
      )
    )
	)
	(helper s nil)
)

(define (contains? list s)
    (cond
        ((null? list) #f)
        ((eq? (car list) s) #t)
        (else (contains? (cdr-stream list) s))))


(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)

; Tail recursion

(define (accumulate combiner start n term)
  (define (accumulate-helper result combiner start n term)
    (if (= n 0)
      result
      (accumulate-helper (combiner result (term n)) combiner start (- n 1) term))
  )
  (accumulate-helper start combiner start n term)
)

; Macros

(define-macro (list-of expr for var in lst if filter-expr)
  (list `map(list `lambda(list var) expr) (list `filter (list `lambda (list var) filter-expr) lst) )
)
