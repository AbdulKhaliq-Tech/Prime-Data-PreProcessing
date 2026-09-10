/**
 * API-client boundary for PrimeProcessing.com.
 *
 * All JS-driven backend calls should go through this module rather than
 * calling `fetch` directly from page scripts. This keeps error handling
 * consistent with the backend's standard envelope and gives later phases
 * one place to add request behavior (e.g. upload progress, retries).
 *
 * Phase 00 scope: the boundary itself and the health check only. No
 * functional (import/cleaning/etc.) endpoints exist yet.
 */
window.PrimeProcessingApi = (function () {
  var API_BASE_URL = '/api';

  function ApiError(message, options) {
    options = options || {};
    this.name = 'ApiError';
    this.message = message;
    this.code = options.code || 'UNKNOWN_ERROR';
    this.status = options.status;
    this.details = options.details;
  }
  ApiError.prototype = Object.create(Error.prototype);

  function request(path, options) {
    options = options || {};
    var method = options.method || 'GET';

    return fetch(API_BASE_URL + path, {
      method: method,
      headers: Object.assign({ 'Content-Type': 'application/json' }, options.headers || {}),
      body: options.body ? JSON.stringify(options.body) : undefined,
    })
      .catch(function () {
        throw new ApiError('Unable to reach the server. Check your connection.', {
          code: 'NETWORK_ERROR',
        });
      })
      .then(function (response) {
        return response
          .json()
          .catch(function () {
            return null;
          })
          .then(function (payload) {
            if (!response.ok) {
              var errorPayload = payload && payload.error;
              throw new ApiError((errorPayload && errorPayload.message) || 'Request failed.', {
                code: (errorPayload && errorPayload.code) || 'REQUEST_FAILED',
                status: response.status,
                details: errorPayload && errorPayload.details,
              });
            }
            return payload;
          });
      });
  }

  function getHealth() {
    return request('/health').then(function (result) {
      return result && result.data;
    });
  }

  return {
    ApiError: ApiError,
    get: function (path) {
      return request(path, { method: 'GET' });
    },
    post: function (path, body) {
      return request(path, { method: 'POST', body: body });
    },
    getHealth: getHealth,
  };
})();
