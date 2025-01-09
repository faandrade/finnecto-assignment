<!-- filepath: /Users/faandrade/Desktop/Finnecto/finnecto-assignment/frontend/src/views/OrdersView.vue -->


<template>
  <div>
    <h1>Orders</h1>
    <div>
      <label for="client-select">Filter by Client:</label>
      <select id="client-select" v-model="selectedClientId" @change="fetchOrders">
        <option value="">All Clients</option>
        <option v-for="client in clients" :key="client.id" :value="client.id">
          {{ client.name }}
        </option>
      </select>
    </div>
    <table>
      <thead>
        <tr>
          <th>Order ID</th>
          <th>Requester</th>
          <th>Description</th>
          <th>Type</th>
          <th>Status</th>
          <th>Date</th>
          <th>Products</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="order in orders" :key="order.id">
          <td>{{ order.id }}</td>
          <td>{{ order.requester.name }}</td>
          <td>{{ order.description }}</td>
          <td>{{ order.type }}</td>
          <td>{{ order.status }}</td>
          <td>{{ new Date(order.date).toLocaleString() }}</td>
          <td>
            <ul>
              <li v-for="product in order.products" :key="product.id">
                {{ product.product.name }} ({{ product.quantity }} x {{ product.price }} {{ product.currency }})
              </li>
            </ul>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
  <v-container>
  <v-row>
    <v-col cols="12">
      <v-btn color="primary" @click="handleClick">Test Vuetify Button</v-btn>
    </v-col>
  </v-row>
</v-container>


</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const orders = ref([]);
const clients = ref([]);
const selectedClientId = ref('');

const handleClick = () => {
console.log('Vuetify button clicked!');
};

const fetchOrders = async () => {
  try {
    const params = selectedClientId.value ? { client_id: selectedClientId.value } : {};
    const response = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/api/orders/`, { params });
    orders.value = response.data;
  } catch (error) {
    console.error('Error fetching orders:', error);
  }
};

const fetchClients = async () => {
  try {
    const response = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/api/clients/`);
    clients.value = response.data;
  } catch (error) {
    console.error('Error fetching clients:', error);
  }
};

onMounted(() => {
  fetchClients();
  fetchOrders();
});
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  border: 1px solid #ddd;
  padding: 8px;
}

th {
  background-color: #f2f2f2;
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}
</style>


