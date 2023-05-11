<div class="col d-flex">
        <div class="row-md-4">
            <img src="/{{ BASE_DIR }}static/images/{{offer.image}}" class="offer-image img-fluid" alt="{{ offer.description }}"/>
        </div>
        <div class="col-md-5 mx-auto px-5 mt-5 py-5">
            <h1>{{ offer.name |upper }}</h1>
           <div class="container-sm d-flex">
               <ul class="list-unstyled my-4">
            <li class="mb-4"> Description: {{ offer.description }}</li>
            <li class="mb-4"> Price: {{ offer.price }} kr.</li>
               </ul>
            </div>


                <label for="chose_pizza">Select a pizza:</label>
            <div class="select-pizza">
                        <select name="pizza" id="chose_pizza">

                        </select>

                <button class="btn btn-dark mt-3" id="buy-offer-btn">Buy offer</button>
        </div>
            </form>
        {% else %}
            <form action="login" method="post">
			    {% csrf_token %}
			    <button class="btn btn-dark mt-3">Login to add to cart</button>
		    </form>
            <form action="create_user" method="post">
			    {% csrf_token %}
			    <button class="btn btn-dark mt-3">Register a new user</button>
		    </form>
        {% endif %}
            </div>
    </div>
    </div>
    </div>