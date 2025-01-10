<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <h1 class="text-h4 mb-6">Purchase Requests</h1>


        <v-select
          v-model="selectedClientId"
          :items="clients"
          item-title="name"
          item-value="id"
          label="Filter by Client"
          clearable
          @update:model-value="fetchOrders"
          class="mb-6"
        ></v-select>


        <v-data-table
      :headers="headers"
      :items="orders"
      class="elevation-1"
    >
    <!-- Template para status con v-chip -->
    <template v-slot:item.status="{ item }">
        <v-chip
          :color="getStatusColor(item.status)"
          text-color="white"
        >
          {{ item.status }}
        </v-chip>
      </template>
      <!-- Template para la fecha con tooltip -->
      <template v-slot:item.date="{ item }">
        <v-tooltip location="top">
          <template v-slot:activator="{ props }">
            <span v-bind="props">
              {{ formatDate(item.date, 'short') }}
            </span>
          </template>
          {{ formatDate(item.date, 'full') }}
        </v-tooltip>
      </template>

      <!-- Template para productos con diálogo expandible -->
      <template v-slot:item.products="{ item }">
        <v-btn
          density="compact"
          variant="text"
          @click="showProductDetails(item.products)"
        >
          {{ `${item.products.length} products` }}
          <v-icon end>mdi-eye</v-icon>
        </v-btn>
      </template>
    </v-data-table>

    <!-- Diálogo para mostrar detalles de productos -->
    <v-dialog v-model="dialogVisible" max-width="600px">
      <v-card>
        <v-card-title class="text-h5 pa-4">
          Product Details
          <v-spacer></v-spacer>
          <v-btn icon="mdi-close" variant="text" @click="dialogVisible = false"></v-btn>
        </v-card-title>
        <v-card-text>
          <v-list>
            <v-list-item
              v-for="product in selectedProducts"
              :key="product.id"
              class="mb-2"
            >
              <v-list-item-title class="font-weight-bold">
                {{ product.product.name }}
              </v-list-item-title>
              <v-list-item-subtitle>
                <v-chip
                  color="primary"
                  size="small"
                  class="mr-2"
                >
                  {{ product.quantity }} units
                </v-chip>
                <v-chip
                  color="success"
                  size="small"
                >
                  {{ formatCurrency(product.price, product.currency) }}
                </v-chip>
              </v-list-item-subtitle>
            </v-list-item>
          </v-list>
        </v-card-text>
      </v-card>
    </v-dialog>
      </v-col>
    </v-row>
  </v-container>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
const orders = ref([]);
const clients = ref([]);
const selectedClientId = ref(null);

// Referencias para el diálogo
const dialogVisible = ref(false);
const selectedProducts = ref([]);

// Headers actualizados con anchos personalizados
const headers = [
  //{ title: 'ID', key: 'id', width: '100px' },
  { title: 'Requester', key: 'requester.name', width: '150px' },
  { title: 'Description', key: 'description' },
  { title: 'Type', key: 'type', width: '100px' },
  { title: 'Status', key: 'status', width: '100px' },
  { title: 'Date', key: 'date', width: '120px' },
  { title: 'Products', key: 'products', width: '120px', align: 'center' },
];

// Funciones de utilidad
const formatDate = (date, style = 'short') => {
  const options = {
    short: {
      day: '2-digit',
      month: '2-digit',
      year: '2-digit'
    },
    full: {
      day: '2-digit',
      month: 'long',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    }
  };

  return new Date(date).toLocaleString(undefined, options[style]);
};

const formatCurrency = (amount, currency) => {
  return new Intl.NumberFormat(undefined, {
    style: 'currency',
    currency: currency,
    currencyDisplay: 'code'
  }).format(amount);
};

const showProductDetails = (products) => {
  selectedProducts.value = products;
  dialogVisible.value = true;
};

const fetchOrders = async () => {
  try {
    const params = selectedClientId.value ? { client_id: selectedClientId.value } : {};
    const response = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/api/orders/`, { params });
    if (Array.isArray(response.data)) {
      orders.value = response.data;
    } else {
      console.error('Unexpected response format:', response.data);
      orders.value = [];
    }
  } catch (error) {
    console.error('Error fetching orders:', error);
    orders.value = [];
  }
};

const fetchClients = async () => {
  try {
    const response = await axios.get(`${import.meta.env.VITE_API_BASE_URL}/api/clients/`);
    if (Array.isArray(response.data)) {
      clients.value = response.data;
    } else {
      console.error('Unexpected response format:', response.data);
      clients.value = [];
    }
  } catch (error) {
    console.error('Error fetching clients:', error);
    clients.value = [];
  }
};

const getStatusColor = (status) => {
      switch (status) {
        case 'APPROVED':
          return 'green';
        case 'REJECTED':
          return 'red';
        case 'APROVING':
          return 'grey';
        default:
          return 'grey';
      }
    };

onMounted(() => {
  fetchClients();
  fetchOrders();
});
</script>


<style scoped>
.v-data-table {
  margin-top: 20px;
}

.v-list-item {
  border-bottom: 1px solid rgba(0, 0, 0, 0.12);
}

.v-list-item:last-child {
  border-bottom: none;
}
</style>
